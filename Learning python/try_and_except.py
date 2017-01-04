try:
    name = input('enter your name ')
    
    #Print('YOOO will get error')

except EOFError:
    print('pressed ctrl+D')
except NameError:
    print("spelling mistake in print statement")
except KeyboardInterrupt:
    print('got a keyboard interrupt')
#else:
    print('entered name was '+name)
finally:
    print('in finally')
