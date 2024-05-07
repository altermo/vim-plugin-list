rm -fr /tmp/gitfile
cd ..
while true;
    cd document/
    python .merg.py
    cd ../other
    set b (python non-documented.py|head -1)
    echo $b|wl-copy
    if not git clone "https://www.github.com/$b" /tmp/gitfile --depth 1 -q
        read
    else
        pushd .
        cd /tmp/gitfile
        bat (fd readme.\* -d 1) -p --paging=always
        popd
        rm -fr /tmp/gitfile
        cd ..
    end
end
