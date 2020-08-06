import random as rnd
from PIL import Image, ImageDraw, ImageFont


#def add_text(w,x,y,size,letter,color):
 #   w.create_text(x, y,font=("Times",size), text=letter,fill=color)
  #  window.create_text(x, y,font=("Times",size), text=letter,fill=color)
  
  
for trial_number in range(3):
  
    def add_text_PIL(draw,x,y,font,letter,color):
        draw.text((x, y), letter,color,font=font)
    
#window = Canvas(t, background = "white", width = big_x, height = big_y) 

    big_x=630
    big_y=650

    x_num=6 #Number letters X-axis
    y_num=6 #Number letters Y-axis

    fractions=[0.10,0.50,0.,0.,0.,0.,0.20,0.20]

    target=True

    trial_type=1
    #trial_number=1

#for x in range(3):

    def make_picture(x_stride,y_stride,x_num,y_num,fractions,target,folder_name,trial_type,trial_number):

        font=ImageFont.truetype("LiberationSerif-Regular.ttf",20)
    
        x_offset=12
        y_offset=12
    
        x_far_side=6
        y_far_side=7
    
        big_x=2*x_offset+x_num*x_stride-x_far_side
        big_y=2*y_offset+y_num*y_stride-y_far_side

    
        image = Image.new("RGB", (big_x, big_y), 'white')
        draw = ImageDraw.Draw(image)
 #   window.pack()
    

        x_c=0   
        y_c=0
    
  
 
        target_letter=["Y"] #Target letter
        color_list=["red","blue","orange","limegreen"] #list colors
    
        letters=[]
        colors=[]

        if target:
            letters.append(target_letter[0]) 
            target_color=rnd.choice(color_list)
            colors.append(target_color)
        
        file=open(folder_name+"/picture_log.txt","a")
        file.write(str(trial_type)+" "+str(trial_number)+" "+str(target)+" "+str(x_stride)+" "+str(y_stride)+" "+str(x_num)+" "+str(y_num)+" "+str(fractions))
        if target:
            file.write(target_color)
        file.write("\n")
        file.close()

        file=open(folder_name+"/images.js","a")
        file.write("var image_"+str(trial_number)+"= {\n")
        file.write("image: \"img/picture_"+str(trial_number)+".png\",\n")
        file.write("colour: \""+str(target_color)+"\",\n")
        file.write("target: "+str(target).lower()+",\n")
        file.write("fractions: "+str(fractions)+",\n")
        file.write("}\n")
        file.close()
    
        list_letters=["T","E","F","L","H","K","V","X"]
 

        letters_num=x_num*y_num
    
        fraction_total=0
    
        for i,letter in enumerate(list_letters):
            fraction_total+=fractions[i]        
            while len(letters)<fraction_total*letters_num:
                letters.append(letter)
                colors.append(rnd.choice(color_list))
 
        rnd.shuffle(letters) #randomly place letters
    
        if target:
            w_index=letters.index("Y")
            colors[w_index] = target_color
    
        while x_c<x_num:
            y_c=0
            while y_c<y_num:
                x=x_offset+x_c*x_stride
                y=y_offset+y_c*y_stride
            #add_text(window,x,y,20,letters.pop(),colors.pop())
                add_text_PIL(draw,x,y,font,letters.pop(),colors.pop())  
                y_c+=1
            x_c+=1
        ImageDraw.Draw(image)

        return image

    x_stride=20
    y_stride=30

    image=make_picture(x_stride,y_stride,x_num,y_num,fractions,target,".",trial_type,trial_number)

    image.save("picture_"+str(trial_type)+"_"+str(trial_number) +".png")
    

# for i in range(3):
