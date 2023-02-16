def findl(data, s, start):
    i = data.find(s, start)
    if i > 0:
        i += len(s)
    return i

def save(fname, no, pre, data, post):
    fp = open(fname%no, 'wb')
    fp.write(pre)
    fp.write(data)
    fp.write(post)
    fp.close()

def main():
    data = open('pit-11-29.html','rb').read()

    i = findl(data, '<body>', 0)
    pre = data[:i]
    data = data[i:]

    i = data.find('</body>', 0)
    post = data[i:]
    data = data[:i]

    fname = 'pit-11-29-%d.html'
    no = 0
    s = '<div class="lamstrone"/>'
    while True:
        i = data.find(s)
        if i < 0:
            save(fname, no, pre, data, post)
            break
        save(fname, no, pre, data[:i], post)
        data = data[i+len(s):]
        no += 1
main()
