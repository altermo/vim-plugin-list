rm -fr /tmp/gitfile
cd ..
while true;
    cd document/
    python .merg.py
    cd ../other
    set b (python non-documented.py|head -1)
    git clone "https://www.github.com/$b" /tmp/gitfile --depth 1 -q
    echo $b|xclip -selection c
    bat /tmp/gitfile/README.* -p --paging=always
    rm -fr /tmp/gitfile
    cd ..
end
