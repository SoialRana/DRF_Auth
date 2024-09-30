from rest_framework_simplejwt.tokens import RefreshToken 

class CustomRefreshToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        token = super().for_user(user)
        token["email"] = user.email  # Add the email to the token payload
        token["user_id"] = user.id   # Ensure user_id is in the token
        print(f"token1: {token}")
        return token
    
    
def get_tokens_for_user(user):
    refresh = CustomRefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    
import jwt
from django.conf import settings
def token_decoder(token):
    if not token:
        print("No token provided")
        return None

    print(f"Token2: {token}")
    try:
        # Decode the token
        decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        print("Decoded Data: ", decoded_data)  # Print the decoded token
        # return decoded_data['user_id']  # Assuming 'user_id' is part of the token payload
        return decoded_data.get('user_id')  # Assuming 'user_id' is part of the token payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        print("Token expired")
        return None
    except jwt.InvalidTokenError:
        # Token is invalid
        print("Invalid token")
        return None


""" def token_decoder(token):
    print("SOmething problem")
    print(f"Token2: {token}")
    try:
        # Decode the token
        decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        print("Decoded Data: ", decoded_data)  # Print the decoded token
        return decoded_data['user_id']  # Assuming 'user_id' is part of the token payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.InvalidTokenError:
        # Token is invalid
        return None """
    
    

