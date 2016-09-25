import time
import os
import math
def alphabet_combine(string,length):
    pa =(('   #    '),(' #   #  '),('#     # '),('# ### # '),('#     # '),('#     # '),('#     # '))
    pb =((' #####  '),('#     # '),('#     # '),('######  '),('#     # '),('#     # '),(' #####  '))
    pc =((' #####  '),('#     # '),('#       '),('#       '),('#       '),('#     # '),(' #####  '))
    pd =(('######  '),('#     # '),('#     # '),('#     # '),('#     # '),('#     # '),('######  '))
    pe =(('####### '),('#       '),('#       '),('######  '),('#       '),('#       '),('####### ')) 
    pf =(('####### '),('#       '),('#       '),('#####   '),('#       '),('#       '),('#       '))
    pg =((' #####  '),('#       '),('#       '),('#   ### '),('#     # '),('#    ## '),(' #### # '))
    ph =(('#     # '),('#     # '),('#     # '),('####### '),('#     # '),('#     # '),('#     # '))
    pi =((' #####  '),('   #    '),('   #    '),('   #    '),('   #    '),('   #    '),(' #####  '))
    pj =(('  ##### '),('     #  '),('     #  '),('     #  '),('     #  '),(' #   #  '),('  ###   '))
    pk =(('#     # '),('#    #  '),('#   #   '),('####    '),('#   #   '),('#    #  '),('#     # '))
    pl =((' #      '),(' #      '),(' #      '),(' #      '),(' #      '),(' #      '),(' #####  '))
    pm =(('#     # '),('##   ## '),('# # # # '),('#  #  # '),('#     # '),('#     # '),('#     # ')) 
    pn =(('#     # '),('##    # '),('# #   # '),('#  #  # '),('#   # # '),('#    ## '),('#     # ')) 
    po =((' #####  '),('#     # '),('#     # '),('#     # '),('#     # '),('#     # '),(' #####  ')) 
    pp =(('######  '),('#     # '),('#     # '),('######  '),('#       '),('#       '),('#       ')) 
    pq =((' #####  '),('#     # '),('#     # '),('#     # '),('#   # # '),('#    #  '),(' #### # ')) 
    pr =(('######  '),('#     # '),('#     # '),('######  '),('#   #   '),('#    #  '),('#     # ')) 
    ps =((' ###### '),('#       '),('#       '),(' #####  '),('      # '),('      # '),('######  '))
    pt =(('####### '),('   #    '),('   #    '),('   #    '),('   #    '),('   #    '),('   #    ')) 
    pu =(('#     # '),('#     # '),('#     # '),('#     # '),('#     # '),('#     # '),(' #####  '))
    pv =(('#     # '),('#     # '),('#     # '),(' #   #  '),(' #   #  '),('  # #   '),('   #    '))
    pw =(('#     # '),('#     # '),('#  #  # '),('#  #  # '),('#  #  # '),('# # # # '),(' #   #  ')) 
    px =(('#     # '),(' #   #  '),('  # #   '),('   #    '),('  # #   '),(' #   #  '),('#     # ')) 
    py =(('#     # '),('#     # '),(' #   #  '),('  # #   '),('   #    '),('   #    '),('   #    '))
    pz =(('####### '),('     #  '),('    #   '),('   #    '),('  #     '),(' #      '),('####### '))
    p_ =(('        '),('        '),('        '),('        '),('        '),('        '),('        '))
    dictionary = {' ':p_,'a':pa,'b':pb,'c':pc,'d':pd,'e':pe,'f':pf,'g':pg,'h':ph,'i':pi,'j':pj,'k':pk,'l':pl,'m':pm,'n':pn,'o':po,'p':pp,'q':pq,'r':pr,'s':ps,'t':pt,'u':pu,'v':pv,'w':pw,'x':px,'y':py,'z':pz}
    screen =[' ']*7 
    move = [' ']
    for k in range(20):
        for j in range(7):
            for i in range(length):
                screen[j]=move[0]*int(math.cos(k)*10+40-2*k)+screen[j]+dictionary[string[i]][j]
            print(screen[j])
            screen = [' ']*7
        time.sleep(0.2)
        os.system('cls')
        print(('\n')*int(math.sin(k)*10+15-k))
    return screen
def main():
    name =input('please input your name:')
    length = len(name)
    name = name.lower()       
    alphabet_combine(name,length)
main()