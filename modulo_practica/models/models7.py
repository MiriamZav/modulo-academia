from odoo import _, api,fields, models

class academia_calificacion(models.Model):
	_name="academia.calificacion"
	_description = "Calificacion"

	name = fields.Many2one("academia.materia", "Materia")
	calificacion = fields.Float("Calificacion", digits=(3,2))
	student_id = fields.Many2one("academia.student", "ID referencia")

	@api.constrains('calificacion')
	def _check_calificacion(self):
		for record in self:
			if record.calificacion < 5 or record.calificacion > 10:
				raise exceptions.ValidatError('La calificacion debe ser mayor a 5 y menor a 10')

class academia_materia(models.Model):
	_name = "academia.materia"
	_description = "Materia"
	
	name = fields.Char("Nombre")

	_sql_constrains = [('name_uniq', 'unique(name)', 'El nombre de la materia debe ser unicos')]
