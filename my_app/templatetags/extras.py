from operator import concat

from django import template



register = template.Library()




@register.simple_tag
def comfort_number(value):

    str1 = str(int(value))    

    beautifulRezult = ""    

    for idx, i in enumerate(reversed(str1)):
            beautifulRezult += i
            if (idx+1) % 3 == 0:               
                beautifulRezult += " "           
            
    return(beautifulRezult[::-1])     


