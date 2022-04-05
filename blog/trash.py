def trash1():
    # traveral 이용했으나 뭔가 구리다. 
    import os
    baseDir = Path(__file__).resolve().parent.parent
    markdownDir = baseDir / 'templates/src/markdown'
    htmlDir = baseDir / 'templates/src/html'
    #메뉴판 변수 만들기 firstDirs / secondDirs 
    firstDirs = [ '메뉴없음']
    for root, dirs, files, rootfd in os.fwalk(markdownDir):
        firstDirs = dirs
        break
    secondDirs = {}
    for firstdir in firstDirs:
        try:
            for root, dirs2, files, rootfd in os.fwalk(markdownDir / firstdir):
                break
            secondDirs[firstdir] = dirs2
        except:
            pass

    for root, dirs3, files in os.walk(markdownDir / 'manual'):
        break
    1
    # traversal markdown -> html
    for root, dirs, files in os.walk(markdownDir):
        for file in files:
            filePath = os.path.join(root, file)
            if filePath.endswith('.md'):
                with open(filePath, 'r') as f:
                    text = f.read()
                    html = markdown.markdown(text)
                with open(f'{htmlDir}/{file[:-2]}html', 'w') as f:
                    f.write(r"{% extends 'blog/write.html' %} {% block main %}")
                    f.write(html)
                    f.write(r"{% endblock main %}")
                pass