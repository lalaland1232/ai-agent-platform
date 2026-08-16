from app.db.models import Session
def create_session(db,hashed_refresh_token,user_id,ip_address,device_name):
    session = Session(
        user_id=user_id,
        hashed_refresh_token=hashed_refresh_token,      
        ip_address=ip_address,
        device_name=device_name,
        revoked_at=None
    )
    db.add(session)
    