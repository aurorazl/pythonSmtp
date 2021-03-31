import os
import time
def clean_kubeflow():
    os.system("kubectl delete ns istio-system knative-serving cert-manager kfserving-system kubeflow auth")
    os.system("kubectl delete validatingwebhookconfigurations --all")
    os.system("kubectl delete mutatingwebhookconfigurations --all")
    os.system("kubectl delete crds --all")
    time.sleep(3)
    os.system("""for ns in istio-system knative-serving cert-manager kfserving-system kubeflow auth;do kubectl get namespace $ns -o json | tr -d "\n" | sed "s/\"finalizers\": \[[^]]\+\]/\"finalizers\": []/" | kubectl replace --raw /api/v1/namespaces/$ns/finalize -f -;done""")

if __name__ == '__main__':
    clean_kubeflow()