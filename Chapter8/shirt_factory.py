def make_shirt(size="Large", message="I love Python"):
    """Customizeable t-shirt ordering function"""
    print(f"You have ordered a size {size} shirt with the text '{message}' printed on it.")

make_shirt()
make_shirt(size="Medium")
make_shirt(message="Say Yes to Michigan", size="Extra Large")