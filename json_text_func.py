import local_database
def converttoobj(new_website, obj_txt):
    """Takes a new website object and some portion of text in an array and parses through
    it to add to the new website object.
    
    obj_text -- ["#\n", "webname=.....\n", "web_url=....\n", "send_key=....\n"]
    new_website -- website object
    """
    #x = index
    obj_txt
    x = 0
    print("phase 1")
    
    if obj_txt[x].split()[0] == '#': 
        print("phase 2")
        obj_txt.pop(0)#init variable to start parsing through website info sets which are lines of text to be used as website objects
        print(obj_txt)
        """to_delete = 0
        procedure_step = 0"""
            #x += 1 # x is line indicator of text files obj, obj_txt
            
        while obj_txt[x].split()[0] != '#': 
            print('repeat phase')
            #skips over 'x', indicating new website info set
            if 'webname=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                holder = " ".join(holder)
                obj_txt.pop(0)
                packer = website_element(holder, holder, "webname")
                
                new_website.setwebname(packer)
                #after the equal, will increment by one to read actual text information
                #new_website.procedure.append(new_website.getwebname())
                """procedure_step += 1
                x += 1"""
            elif 'web_url=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setweburl(packer)
                new_website.append_command(new_website.getweburl())
                """procedure_step += 1
                x += 1"""
            elif 'addcart=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setaddcart(packer)
                new_website.append_command(new_website.getaddcart())
                """procedure_step += 1
                x += 1"""
            elif 'checkout=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setcheckout(packer)
                new_website.append_command(new_website.getcheckout())
                """procedure_step += 1
                x += 1"""
            elif 'gocart=' in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setgotocart(packer)
                new_website.append_command(new_website.getgocart())
                """procedure_step += 1
                x += 1"""
            elif "send_key=" in obj_txt[x]:
                holder = obj_txt[x][(obj_txt[x].find('=')+1):len(obj_txt[x])].split()
                needclear = True if holder[-1] == 'true' else False
                holder = holder[0:-1]
                obj_txt.pop(0)
                keys = holder[1:-1]
                space = " "
                keys = space.join(keys)
                packer = website_element(holder[0], keys, holder[-1])
                packer.need_clear = needclear
                new_website.append_command(packer)
            
            else:
                holder = obj_txt[x].split()
                obj_txt.pop(0)
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.append_command(packer)
                """procedure_step += 1"""
            try:
                if len(obj_txt[x].split()[0].split()) <= 0:
                    break
            except:
                break
                
            
        #return [new_website, x]
        #index = x
        #wobj_txt = obj_txt
        print('leftover ', obj_txt, "\n", [i.name for i in new_website.getprocedure()])
        return new_website
#def saveobj(website):

 
def convert_dict_to_obj(dict, new_website):
    """Takes a json iterable dictionary and a new website object 
    and reads through json dictionary to create website object
    
    dict -- JSON iterable"""
    print('dict')
    for i in dict:
        print(i)
        if 'webname' in i:
                holder = dict.get(i).split()
                packer = website_element(holder[0], holder[0], "webname")
                
                new_website.setwebname(packer)
                #after the equal, will increment by one to read actual text information
                #new_website.procedure.append(new_website.getwebname())
                """procedure_step += 1
                x += 1"""
        elif 'web_url' in i:
                holder = dict.get(i).split()
                packer = website_element(holder[0], holder[1], holder[2])
                new_website.setweburl(packer)
                new_website.append_command(new_website.getweburl())
                """procedure_step += 1
                x += 1"""
        elif 'addcart' in i:
            holder = dict.get(i).split()
            
            packer = website_element(holder[0], holder[1], holder[2])
            new_website.setaddcart(packer)
            new_website.append_command(new_website.getaddcart())
            """procedure_step += 1
            x += 1"""
        elif 'checkout' in i:
            holder = dict.get(i).split()
            
            packer = website_element(holder[0], holder[1], holder[2])
            new_website.setcheckout(packer)
            new_website.append_command(new_website.getcheckout())
            """procedure_step += 1
            x += 1"""
        elif 'gocart' in i:
            holder = dict.get(i).split()
            
            packer = website_element(holder[0], holder[1], holder[2])
            new_website.setgotocart(packer)
            new_website.append_command(new_website.getgocart())
            """procedure_step += 1
            x += 1"""
        elif "send_key" in i:
            holder = dict.get(i).split()
            needclear = True if holder[-1] == 'true' else False
            holder = holder[0:-1]
            
            keys = holder[1:-1]
            space = " "
            keys = space.join(keys)
            packer = website_element(holder[0], keys, holder[-1])
            packer.need_clear = needclear
            new_website.append_command(packer)
        
        else:
            holder = dict.get(i).split()
            print(holder)
            packer = website_element(holder[0], holder[1], holder[2])
            new_website.append_command(packer)
            """procedure_step += 1"""
    return new_website
        
def convertalltoobj(obj_txt):
    """obj_txt is list of strings taken from gui for new website
    
    obj_txt -- a list of lines of text from a text file"""
    copy_obj_txt = obj_txt[:]
    print('copy ', copy_obj_txt)
    print('og ', obj_txt)
    websites = {}
    while len(copy_obj_txt) > 0 and len(copy_obj_txt[0].split()) > 0:
        print("convert all loop")
        new_website = website_dataobj()
        new_website = converttoobj(new_website, copy_obj_txt)
        websites[new_website.getwebname().name] = new_website 
        print("done with loop")
    print("done")
    print('copyf ', copy_obj_txt)
    print('ogf ', obj_txt) 
    return websites