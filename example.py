import wxhtmlwidgets
import wx

app = wx.App()
frame = wxhtmlwidgets.AccessibleHTMLDialog(None, wx.ID_ANY, "Test")
frame.SetPage("<html><body><h1>Terms Of Service</h1><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p><p>Fusce scelerisque placerat accumsan. Curabitur quis nisi nec leo tincidunt facilisis vitae quis est.</p><p>Nullam luctus scelerisque orci eu porta. Fusce vel tempor velit.</p><p>Cras bibendum ante eget dui consectetur, eget finibus justo ultricies. Curabitur sollicitudin molestie maximus.</p><p>Aliquam sed dolor ullamcorper, ornare odio non, efficitur ligula. Morbi non massa nunc. Nulla eget sodales erat.</p><p>Phasellus felis mauris, congue eu pulvinar non, fringilla quis urna. Etiam eget dapibus elit. Integer pretium dui quam, eu maximus velit rutrum vitae. Morbi nulla erat, blandit id viverra a, interdum lacinia dui.</p></body></html>")
frame.AddButton("Decline",  55)
frame.AddButton("Agree", 20)
result = frame.ShowModal()
frame.Destroy()
print(result)
if result == 20:
    print("User accepted")
if result == 55:
    print("User diclined")
app.MainLoop()
