import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()


      cleaned_text = ''
      symbols = False
      for item in html:
          if item == '<':
              symbols = True
          elif item == '>':
              symbols = False
          elif not symbols:
              cleaned_text += item

      with codecs.open(result_file, 'w', 'utf-8') as new_file:
          new_file.write(cleaned_text.strip())


delete_html_tags('draft.html')
