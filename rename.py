import glob, os, sys

def rename(dir, pattern, start_ep):
    for path_and_filename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(path_and_filename))
        split_title = title.split(" - ")
        ep_num = int(start_ep) + int(split_title[0])
        new_title = "%s - %s%s" % (ep_num, split_title[1], ext)
        print(new_title)
        os.rename(path_and_filename, os.path.join(dir, new_title))

rename('./', r'*.avi', sys.argv[1])
