import subprocess

def get_commit_info(commit_hash):
    try:
        # 使用 git show 命令获取提交信息
        result = subprocess.run(
            ['git', 'show', '--pretty=fuller', '-s', commit_hash],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        if result.returncode != 0:
            raise Exception(f"Error: {result.stderr}")
        
        # 解析输出以获取作者和提交者信息
        output = result.stdout
        author_line = None
        committer_line = None
        
        for line in output.splitlines():
            if line.startswith('Author:'):
                author_line = line
            elif line.startswith('Commit:'):
                committer_line = line
        
        if not author_line or not committer_line:
            raise Exception("Could not find author or committer information.")
        
        # 提取作者和提交者的姓名和电子邮件
        author_info = author_line.split(':', 1)[1].strip()
        committer_info = committer_line.split(':', 1)[1].strip()
        
        return {
            'author': author_info,
            'committer': committer_info
        }
    
    except Exception as e:
        return {'error': str(e)}

# 示例使用
commit_hash = '46c3c703cbb2e7bae5baa6baa7ea0208b454f4a8'
info = get_commit_info(commit_hash)
print(info)