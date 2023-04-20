def get_richview_theme():
    richview_theme ={
            'config': {
                'background': '#FAF9F6',
                'view': {
                    'stroke': 'transparent',
                    'width': 450,
                    'height': 300,
                },
                'axis': {
                    'gridColor': '#CCC1B7',
                    'gridWidth': 0.2,
                    'grid':True,
                    'labelFont': 'Lora, Palatino Linotype, Cambria, Century Gothic',
                    'labelFontSize': 9.6,
                    'labelColor': '#4D4845',
                    'titleFont': 'Lora, Palatino Linotype, Cambria, Century Gothic',
                    'titleFontSize': 0,
                    'titleColor': '#4D4845',
                    'domainColor': '#4D4845',
                    'domainWidth': 0.2,
                    'tickColor': '#4D4845',
                    'tickWidth': 0.2,
                    'tickLength': 3.5

                },
                'axisX': {'grid':False},
                'axisY': {'line':None, 'domainOpacity':0},

                'legend': {
                    'titleFontSize': 0,
                    'orient': 'top',
                    'direction':'horizontal',

                },
            'title': {

                'anchor': 'start',
                'align':'left',
                'fontWeight':'normal',
                'dx': 40,
                'font': 'Lora, Palatino Linotype, Cambria, Century Gothic',
            },
                'range': {
                    'category': [
                        "#186cac", "#81e7cc", "#eec8f1", "#dce475", "#86ec5a", "#eb70d5", "#829951", "#5a3386",
                        "#a50fa9", "#4ba40b"
                    ]
                }
            }
        }
    return richview_theme

def scientific_theme():
    font = 'Cambria',
    fontsize = 14
    fontColor = '#000000',
    color_theme = ['#00376C', '#8A0F0F', '#00572C', '#6c0037', '#6c3500', '#d1d1c2']
    width = 620
    height = 375

    return {
        'config': {
            'padding': {
                'left': 0,
                'top': 0,
                'right': 0,
                'bottom': 5
            },
            'autosize': {
                'type': 'fit-x',
                'resize': False,
                'contains': 'padding'
            },
            'view': {
                'width': width,
                'height': height,
                'stroke': True,
                'strokeWidth': 1,
                'strokeDash': [0],
                'padding': {
                'left': 0,
                'top': 0,
                'right': 0,
                'bottom': 5,
                'orient':'right'
            }
            },
            'title': {
                'fontSize': fontsize,
                'font': font,
                'anchor': 'start',
                'fontColor': fontColor,
                'fontWeight':'normal'
            },
            'axis': {
                'domain': False,
                'domainColor': fontColor,
                'grid': False,
                'gridDash': [10],
                'gridWidth': 1,
                'gridOpacity': 0.3,
                'gridColor': fontColor,
                'labelFont': font,
                'titleFont': font,
                'titleFontSize': fontsize,
                'labelFontSize': fontsize,
                'labelOverlap': True,
                'labelAngle': 0,
                'titleAngle': 0,
                'domainOpacity': 1,
                'tickColor': font,
                'tickSize': 5,
                'tickWidth': 1,
                'labelSeparation': 0,
                'titleFontWeight': 'normal',
                'zindex': -10,
                'labelLimit': 999
            },
            'header': {
                'labelFont': font,
                'titleFont': font,
                'titleFontSize': 0,
                'labelFontSize': fontsize
            },
            'legend': {
                'labelFont': font,
                'titleFont': font,
                'titleFontSize': fontsize,
                'labelFontSize': fontsize
            },
            'axisY': {
                'grid': True,
                'titlePadding': 10,
                'titleAngle': -90,

            },
            'range': {
                'category':
                color_theme,
                'diverging':
                color_theme[:2],
                'ordinal': [
                    '#00376c'
                    '#194b7a'
                    '#325e89'
                    '#4c7398'
                    '#6687a6'
                    '#7f9bb5'
                    '#99afc4'
                    '#b2c3d2'
                    '#ccd7e1'
                    '#e5ebf0'
                ]
            },
            'mark': {
                'color': color_theme[0],
            },
            'text': {
                'fontSize': fontsize,
                'font': font
            },
            'cell': {
                'stroke': True,
                'strokeColor': font,
                'strokeWidth': 1,
                'strokeOpacity': 1
            }
        }
    }