import os


def renameFiles(dir, dstName, suffixSize, srcExt, dstExt, namePart):
    beg, end = namePart[0], namePart[1]
    count = 0
    for fileName in os.listdir(dir):
        src = os.path.join(dir, fileName)
        if os.path.isfile(src) and src.endswith(srcExt):
            namePart = fileName.strip(srcExt)[beg-1:end]
            count += 1
            if suffixSize > 0:
                targetName = f"%s%s%0{suffixSize}d%s" % (namePart, dstName, count, dstExt)
            else:
                targetName = f"%s%s%s" % (namePart, dstName, dstExt)
            print(fileName, "->", targetName)
            os.rename(src, os.path.join(dir, targetName))


renameFiles("/var/tmp/mydir", "dst", 2, ".txt", ".xtx", [1, 4])
# renameFiles("/var/tmp/mydir", "", 0, ".xtx", ".txt", [1, 4])
