import sys,os,re

userName='TQCAI'
password='password'

gitignore='''
venv
.idea
__pycache__
'''

def exeCmd(cmd):
    cmds=cmd.split('\n')
    for c in cmds:
        os.system(c)

def getRepoName(url):
    pattern = r"https://github.com/(?P<user>.*)/(?P<repo>.*)"
    m = re.match(pattern, url)
    return m.group('repo')

def createReadMe(dir,url):
    repo=getRepoName(url)
    readme=f'''
# {repo}

---

url={url}
>I'am as nice person ,please star me
    '''

    fileName=f'{dir}/README.md'
    if not os.path.exists(fileName):
        with open(fileName,'w') as f:
            f.write(readme)

if __name__ == '__main__':
    print('git init directory: ',sys.argv[1])
    dir=sys.argv[1]
    if os.path.exists(f'{dir}/.git'):#已经初始化
        pass
    else:
        with open('.gitignore', 'w') as f:
            f.write(gitignore)
        url=input('input github repository URL: ')
        if url=='':
            exit(0)
        createReadMe(dir,url)
        suffix=url.replace('https://','')
        https=f'https://{userName}:{password}@{suffix}.git'
        cmd=f'''
            git init
            git remote add origin {https}
            '''
        exeCmd(cmd)
    #公操作
    cmd='''
        git add -A
        git commit -m "commit"
        git push origin master
        '''
    exeCmd(cmd)
