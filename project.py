input=input("\n\nWould you like to shut down this computer   \n   ")
def shutdown(choice):
    choice=choice.lower() #tip i learnt from youtube

    if choice=="yes":
        print("\nShutting down.....")
    elif choice=="no":
        print("\nPowering Up.....")
    else:
        print("\nSorry, input unclear")

shutdown(input)