import auth_service


if __name__ == "__main__":
    print("Backup service starting...")
    auth_service.main(enable_crash=False)