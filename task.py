from RPA.Robocorp.Vault import FileSecrets

test = FileSecrets()

var = test.get_secret("test")
print(var["key"])
var["key"] = "value_updated"
test.set_secret(var)
print(var["key"])