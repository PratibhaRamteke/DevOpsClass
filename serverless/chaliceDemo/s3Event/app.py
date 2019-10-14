from chalice import Chalice

app = Chalice(app_name='s3Event')
app.debug = True

@app.on_s3_event(bucket='s3eventbucket1',
                 events=['s3:ObjectCreated:*'])
def handle_s3_event(event):
    app.log.debug("Received event for bucket: %s, key: %s",
                  event.bucket, event.key)
