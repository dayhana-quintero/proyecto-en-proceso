from flask_wtf import FlaskForm 
from wtforms import ( 
    StringField, 
    DecimalField, 
    BooleanField, 
    DateField, 
    SubmitField 
) 

from wtforms.validators import DataRequired, Length, NumberRange, Optional 

class InsumoForm(FlaskForm): 
    codigo = StringField( 
        'Código', 
        validators=[ 
            DataRequired(message="El código es obligatorio"), 
            Length(max=50) 
        ] 
    ) 

    descripcion = StringField( 
        'Descripción', 
        validators=[ 
            DataRequired(message="La descripción es obligatoria"), 
            Length(max=200) 
        ] 
    ) 

    lote = StringField( 
        'Lote', 
        validators=[ 
            Optional(), 
            Length(max=50) 
        ] 
    ) 

    invima = StringField( 
        'Registro Invima', 
        validators=[ 
            Optional(), 
            Length(max=50) 
        ] 
    ) 

    valor = DecimalField( 
        'Valor', 
        validators=[ 
            DataRequired(message="El valor es obligatorio"), 
            NumberRange(min=0) 
        ], 
        places=2 
    ) 

    iva = BooleanField('Aplica IVA') 
    fecha_vencimiento = DateField( 
        'Fecha de vencimiento', 
        validators=[Optional()], 
        format='%Y-%m-%d' 
    ) 
    
    submit = SubmitField('Guardar') 
