
from psychopy import gui




#class InputBox(object):

myDlg = gui.Dlg(title="OpenBCI Menu")
myDlg.addText('Subject info')
myDlg.addField('Participant')#0
myDlg.addField('Session', 001)#1
myDlg.addField('Port', '/dev/ttyACM0')#2
myDlg.addText('Visual Options')
myDlg.addField('Plots:', choices=["None", "Multi_Plot", "FFT",
"Spectogram"])#3
myDlg.addText('Experiment Choices')
myDlg.addField('Experiments', choices=["None", "SSVEP", "ERP",
	"Motor_Imagery"])#4
myDlg.show()  # show dialog and wait for OK or Cancel
if myDlg.OK:  # then the user pressed OK
  thisInfo = myDlg.data
  options = {'participant': thisInfo[0], 'session': thisInfo[1],'port': thisInfo[2], 'plot': thisInfo[3],'experiment': thisInfo[4]}
  fname = '%s_%s.csv' %(options['participant'],    options['session'])
  port = options['port']
		
		
		#iterate through dictionary to see if Function is called
		#right now just using print statements, soon insert actual python scripts
  for value in options.itervalues():
    if value == 'Multi_Plot':
      import multi_plotter
      multi=multi_plotter.MultiPlotter()
      multi.start(1)				
    elif value == 'FFT':
      import raw_plotter
      fft_plot=fft_plotter.FFTPlotter()
      fft_plot.start()
    elif value == 'Spectogram':
      import spectral_plotter
      specgram=spectral_plotter.SpectralPlotter()
      specgram.start(1)
            
      print 'Spectogram'
    elif value == 'SSVEP':
      import run_ssvep
    elif value == 'ERP':
      print 'ERP'
    elif value == 'Motor_Imagery':
      import motorimagery
    
			

else:
  print 'user cancelled'
