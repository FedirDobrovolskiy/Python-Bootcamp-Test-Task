def convert(var):
    temp = var.split()
    path = ''
    for i in temp:
        path += i + '-'
    ans = "/home/user/" + path + "1.gif"
    return ans


print(convert("TikTok-example"))
