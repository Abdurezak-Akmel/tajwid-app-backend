from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import EmailStr
from app.core.config import settings
from pathlib import Path

# 1. Initialize Connection Config
mail_conf = ConnectionConfig(
    MAIL_USERNAME=settings.mail_username,
    MAIL_PASSWORD=settings.mail_password,
    MAIL_FROM=settings.mail_from,
    MAIL_PORT=settings.mail_port,
    MAIL_SERVER=settings.mail_server,
    MAIL_FROM_NAME=settings.mail_from_name,
    # Use SSL/TLS for port 465, otherwise use STARTTLS
    MAIL_STARTTLS=False if settings.mail_port == 465 else True,
    MAIL_SSL_TLS=True if settings.mail_port == 465 else False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

async def send_email(
    subject: str, 
    email_to: EmailStr, 
    body: str, 
    is_html: bool = True
):
    """
    Standard utility to send an email asynchronously.
    """
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body,
        subtype=MessageType.html if is_html else MessageType.plain
    )

    fm = FastMail(mail_conf)
    await fm.send_message(message)

async def send_reset_password_email(email_to: str, token: str):
    """
    Specific helper for password reset.
    """
    subject = "Tejwid App - Reset Your Password"
    body = f"""
    <h3>Password Reset Request</h3>
    <p>Hello,</p>
    <p>We received a request to reset your password. Use the token below to complete the process:</p>
    <p><strong>{token}</strong></p>
    <p>This token will expire in 15 minutes.</p>
    <p>If you did not request this, please ignore this email.</p>
    """
    await send_email(subject, email_to, body)

async def send_verification_email(email_to: str, token: str):
    """
    Specific helper for email verification.
    """
    subject = "Tejwid App - Verify Your Account"
    # The base URL is now pulled from your environment settings
    verify_url = f"{settings.api_base_url}/auth/verify?token={token}"
    
    body = f"""
    <h3>Welcome to Tejwid App!</h3>
    <p>Please click the button below to verify your email address and activate your account:</p>
    <div style="margin: 20px 0;">
        <a href="{verify_url}" 
           style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
           Verify Account
        </a>
    </div>
    <p>If the button doesn't work, copy and paste this link into your browser:</p>
    <p>{verify_url}</p>
    """
    await send_email(subject, email_to, body)
