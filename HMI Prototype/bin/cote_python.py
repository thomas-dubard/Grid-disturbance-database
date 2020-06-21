from py4j.java_gateway import JavaGateway

gateway = JavaGateway()
app = gateway.entry_point
app.setVisible(True)

while True:
    save = app.dist.hasSaved
    if save:
        thing_to_save = app.dist.saving
        ## Perform the saving in the database
        print(thing_to_save)
