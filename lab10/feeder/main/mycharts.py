from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import HorizontalBarChart

from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.lineplots import ScatterPlot
from reportlab.lib import colors
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.widgets.markers import makeMarker


class MyLineChartDrawing(Drawing):
    def __init__(self, width=1800, height=200, *args, **kw):
        Drawing.__init__(*((self,width,height)+args),**kw)
        self.add(LinePlot(), name='chart')

        self.add(String(200,80,''), name='title')

        self.chart.x = 70
        self.chart.y = 20
        # self.chart.width = self.width - 100
        # self.chart.height = self.height
        self.chart.lines[0].strokeColor = colors.blue
        self.chart.lines[1].strokeColor = colors.green
        self.chart.lines[2].strokeColor = colors.yellow
        self.chart.lines[3].strokeColor = colors.red
        self.chart.lines[4].strokeColor = colors.black
        self.chart.lines[5].strokeColor = colors.orange
        self.chart.lines[6].strokeColor = colors.cyan
        self.chart.lines[7].strokeColor = colors.magenta
        self.chart.lines[8].strokeColor = colors.brown
    
        self.chart.fillColor = colors.white
        self.title.fontName = 'Times-Roman'
        self.title.fontSize = 24
        self.chart.data = [((0, 50), (100,100), (200,200), (250,210), (300,300), (400,500))]
        self.chart.xValueAxis.labels.fontSize = 12
        self.chart.xValueAxis.forceZero = 0
        self.chart.xValueAxis.gridEnd = 115
        self.chart.xValueAxis.tickDown = 3
        self.chart.xValueAxis.visibleGrid = 1
        self.chart.yValueAxis.tickLeft = 3
        self.chart.yValueAxis.labels.fontName = 'Times-Roman'
        self.chart.yValueAxis.labels.fontSize = 12
        self.title.x = 50
        self.title.y = 80
        self.title.textAnchor ='middle'
        self.add(Legend(),name='Legend')
        self.Legend.fontName = 'Times-Roman'
        self.Legend.fontSize = 12
        self.Legend.x = self.width
        self.Legend.y = 85
        self.Legend.dxTextSpace = 5
        self.Legend.dy = 5
        self.Legend.dx = 5
        self.Legend.deltay = 5
        self.Legend.alignment ='right'
        self.add(Label(),name='XLabel')
        self.XLabel.fontName = 'Times-Roman'
        self.XLabel.fontSize = 24
        self.XLabel.x = 320
        self.XLabel.y = 10
        self.XLabel.textAnchor ='middle'
        #self.XLabel.height = 20
        self.XLabel._text = ""
        self.add(Label(),name='YLabel')
        self.YLabel.fontName = 'Times-Roman'
        self.YLabel.fontSize = 20
        self.YLabel.x = 40
        self.YLabel.y = 160
        self.YLabel.angle = 90
        self.YLabel.textAnchor ='middle'
        self.YLabel._text = ""
        self.chart.yValueAxis.forceZero = 1
        self.chart.xValueAxis.forceZero = 1