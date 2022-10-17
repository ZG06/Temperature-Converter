from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.core.window import Window


Window.size = (dp(350), dp(550))


class ConverterWidget(Widget):
   def clear(self):
      self.ids.input_data.text = '0'

   def number_input(self, number):
      prev_number = self.ids.input_data.text

      if prev_number == '0': 
         self.ids.input_data.text = ''
         self.ids.input_data.text = f'{number}'
      else:
         self.ids.input_data.text = f'{prev_number}{number}'

   def remove_last(self):
      prev_number = self.ids.input_data.text
      prev_number = prev_number[:-1]

      if len(prev_number) != 0:
         self.ids.input_data.text = prev_number
      else:
         self.ids.input_data.text = '0'

   def swap_signs(self):
      prev_number = self.ids.input_data.text

      if '-' in prev_number and prev_number != '0':
         self.ids.input_data.text = f'{prev_number.replace("-", "")}'
      else:
         if prev_number != '0':
            self.ids.input_data.text = f'-{prev_number}'

   def dot(self):
      prev_number = self.ids.input_data.text

      if '.' in prev_number:
         pass
      else:
         self.ids.input_data.text = f'{prev_number}.'

   def convert(self):
      inp = self.ids.input_unit.text
      outp = self.ids.output_unit.text
      data = self.ids.input_data.text

      try:

         if inp == '°C' and outp == '°F':
            return eval(str(float(data) * 1.8 + 32))

         elif inp == '°C' and outp == '°K':
            return eval(str(float(data) + 273.15))
            
         elif inp == '°C' and outp == '°R':
            return eval(str(float(data) * 1.8 + 491.67))
            
         elif inp == '°C' and outp == '°Re':
            return eval(str(float(data) * 0.8))

         elif inp == '°F' and outp == '°C':
            return eval(str((float(data) - 32) * 5/9))

         elif inp == '°F' and outp == '°K':
            return eval(str((float(data) - 32) * 5/9 + 273))

         elif inp == '°F' and outp == '°R':
            return eval(str(float(data) + 459.67))

         elif inp == '°F' and outp == '°Re':
            return eval(str((float(data) - 32) * 4/9))

         elif inp == '°K' and outp == '°C':
            return eval(str(float(data) - 273.15))

         elif inp == '°K' and outp == '°F':
            return eval(str((float(data) - 273.15) * 9/5 + 32))

         elif inp == '°K' and outp == '°R':
            return eval(str(float(data) * 1.8))

         elif inp == '°K' and outp == '°Re':
            return eval(str(float(data) * 1.25 + 273.15))

         elif inp == '°R' and outp == '°C':
            return eval(str((float(data) - 491.67) * 5/9))

         elif inp == '°R' and outp == '°F':
            return eval(str(float(data) - 459.67))
            
         elif inp == '°R' and outp == '°K':
            return eval(str(float(data) / 1.8))

         elif inp == '°R' and outp == '°Re':
            return eval(str((float(data) - 32 - 459.67) / 2.25))

         elif inp == '°Re' and outp == '°C':
            return eval(str(float(data) * 1.25))

         elif inp == '°Re' and outp == '°F':
            return eval(str(float(data) * 2.25 - 32))

         elif inp == '°Re' and outp == '°K':
            return eval(str(float(data) * 1.25 + 273.15))

         elif inp == '°Re' and outp == '°R':
            return eval(str(float(data) * 2.25 + 32 + 459.67))

         elif inp == '°C' and outp == '°C':
            return data

         elif inp == '°F' and outp == '°K':
            return data

         elif inp == '°K' and outp == '°K':
            return data

         elif inp == '°R' and outp == '°R':
            return data
         
         elif inp == '°Re' and outp == '°Re':
            return data

         elif inp == 'Unit' or outp == 'Unit':
            return 'Error'
      
      except ValueError:
         return 'Error'
         
   def output(self):
      self.ids.output_data.text = f'{self.convert()}'


class ConverterApp(App):
   def build(self):
      return ConverterWidget()


if __name__ == '__main__':
   ConverterApp().run()
