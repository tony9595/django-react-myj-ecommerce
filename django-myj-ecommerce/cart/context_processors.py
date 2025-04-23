from .cart import Cart


# dev_17
def cart(request):

    # cart.decrypt_all_sessions()
    print("카트함수호출")

    return {"cart": Cart(request)}
