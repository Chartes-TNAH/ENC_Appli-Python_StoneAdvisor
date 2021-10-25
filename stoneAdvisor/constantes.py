from warnings import warn

# Secret key
SECRET_KEY = "Les archéologues ne fouillent pas des dinosaures"

# Warning in case the secret key hasn't changed
if SECRET_KEY == "Les archéologues ne fouillent pas des dinosaures":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)
