import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()


      cleaned_text = re.sub(r'<.*?>', '', html)
      with codecs.open(result_file, 'w', 'utf-8') as new_file:
          new_file.write(cleaned_text.strip())


delete_html_tags('draft.html')
