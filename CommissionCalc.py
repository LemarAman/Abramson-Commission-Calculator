'''
1-50 evals generated - $0.20 per eval
51+ evals generated - $1 per eval

1-15 evals turned signed client - $1 per client
16+ evals turned signed client - $3 per client

test nums: 46 evals generated $9.20, 20 signed ct $30.
76 eval gen $36, 28 signed ct $54.
'''
import PySimpleGUI as sg
import os

layout = [
    [sg.Text('Please enter evals generated, and evals turned signed client')],
    [sg.Text('Evals Generated', size=(15, 1)), sg.InputText()],
    [sg.Text('Evals Turned Signed Client', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('Ross The Boss Commission Calculator', layout)
event, values = window.read()

window.close()

# evalsGenerated = int(input("How many evaluations generated? "))
evalsGenerated = int(values[0])
signedClients = int(values[1])
# signedClients = int(input("How many evaluations turned signed client? "))

totalEvalCommission = 0
totalSignedCommission = 0

if evalsGenerated <= 50:
    for i in range(1, evalsGenerated + 1):
        totalEvalCommission = i * 0.2

if evalsGenerated > 50:
    for i in range(50, evalsGenerated + 1):
        totalEvalCommission = (i + 10) - 50

if signedClients <= 15:
    for i in range(1, signedClients + 1):
        totalSignedCommission = i

if signedClients > 15:
    for i in range(16, signedClients + 1):
        totalSignedCommission = (i * 3) - 30

totalCommissions = totalEvalCommission + totalSignedCommission

layout2 = [
    [sg.Text('Commissions')],
    [sg.Text("Eval commissions are ", size=(30, 1)), sg.Text("$" + (str(round(totalEvalCommission,2))))],
    [sg.Text('Signed client commissions are ', size=(30, 1)), sg.Text("$" + str(totalSignedCommission))],
    [sg.Text('Total commissions ', size=(30, 1)), sg.Text("$" + str(totalCommissions))],
    [sg.Exit()]
]
window = sg.Window('Ross The Boss Commission Calculator', layout2)
event, values = window.read()

window.close()
