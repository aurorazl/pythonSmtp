a = """
        bash -c '
            export DEBIAN_FRONTEND=noninteractive; 
            if ! [ -x \"$(command -v code-server)\" ];then 
                apt-get update && umask 022
                version="$(curl -fsSLI -o /dev/null -w "%s" https://github.com/cdr/code-server/releases/latest)"                                                                                                                         
                version="${version#https://github.com/cdr/code-server/releases/tag/}"
                version="${version#v}"
                echo "$version"
                curl -fOL https://github.com/cdr/code-server/releases/download/v$version/code-server_${version}_amd64.deb
                sudo dpkg -i code-server_${version}_amd64.deb
            fi
            && cd /home/%s
            && runuser -l %s  -c "
                nohup code-server --port %s --host 0.0.0.0 --auth none &>/job/vscode/log &
            "
        '
    """% ("%{url_effective}","a", "b", "c")
print(a)
print(sorted([1,2,4,3],reverse=True))
import numpy as np

a = np.zeros((1,3,3,3))
a = a[0,:]
print(a.shape)
print(1>2 and False)