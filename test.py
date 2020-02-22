from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from prometheus_client.twisted import MetricsResource
import threading
import time
from prometheus_client import Histogram
import sys
import traceback
import signal

def dumpstacks(signal, frame):
    id2name = dict([(th.ident, th.name) for th in threading.enumerate()])
    code = []
    for threadId, stack in sys._current_frames().items():
        code.append("\n# Thread: %s(%d)" % (id2name.get(threadId,""), threadId))
        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('File: "%s", line %d, in %s' % (filename, lineno, name))
            if line:
                code.append("  %s" % (line.strip()))
    print("\n".join(code))
    sys.stdout.flush()
    sys.stderr.flush()

def register_stack_trace_dump():
    signal.signal(signal.SIGTRAP, dumpstacks)

class HealthResource(Resource):
    def render_GET(self, request):
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return "<html>Ok</html>".encode("utf-8")

def exporter_thread(port):
    root = Resource()
    root.putChild(b"metrics", MetricsResource())
    root.putChild(b"healthz", HealthResource())
    factory = Site(root)
    try:
        reactor.listenTCP(port, factory)
        reactor.run(installSignalHandlers=False)
    except Exception as e:
        exitcode = 1
        exception = e
        exc_traceback = ''.join(traceback.format_exception(*sys.exc_info()))


def setup_exporter_thread(port):
    t = threading.Thread(target=exporter_thread, args=(port,),
            name="exporter")
    t.start()
    return t

manager_iteration_histogram = Histogram("manager_iteration_latency_seconds",
        "latency for manager to iterate",
        buckets=(2.5, 5.0, 10.0, 20.0, 40.0, 80.0, 160.0, float("inf")),
        labelnames=("name",))

def Run():
    register_stack_trace_dump()
    while True:
        with manager_iteration_histogram.labels("command_manager").time():
            print("now")
            time.sleep(3)

try:
    setup_exporter_thread(8000)
    Run()
except Exception as e:
    print("exiting",e)
