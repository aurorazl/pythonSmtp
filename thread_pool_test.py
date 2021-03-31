
def fortran_callback(future):
    print(dir(future))
    print(future.result())
    print(future.run_type, future.jid)
    return "Fortran finished executing"

def test():
    return 111

def fortran_execute():

    from concurrent.futures import ProcessPoolExecutor as Pool

    args = "sleep 2; echo complete"

    pool = Pool(max_workers=1)
    future = pool.submit(test)
    future.run_type = "run_type"
    future.jid = "jid"
    future.add_done_callback(fortran_callback)

    print("Fortran executed")
    return 111

if __name__ == '__main__':
    import subprocess
    fortran_execute()