
const custom_prefix = '#step';

// this will cut up a single long page into multiple 'subpages' that can be navigated through
// sphinx will give them the hash #{text} where text is the title of the section or #id{number} if the title is a number.
// this script will find the index of that section and convert it to #step{number} and show that section.

function appendHtml(el, str) {
  var div = document.createElement('div'); //container to append to
  div.innerHTML = str;
  while (div.children.length > 0) {
    el.appendChild(div.children[0]);
  }
}


window.onload = (event) => {
  // Fix to add languea selector button to header:
  // https://github.com/executablebooks/sphinx-book-theme/issues/797
//  header.append("<div>L</div>");
  update_from_hash();
  get_articles();
  load_lazy_imgs();  
};

function update_from_hash(){
  // Get the id of the active section
  let id = 1;
  if(window.location.hash){
    const hash = window.location.hash;
    if(hash.startsWith(custom_prefix)){
    id = parseInt(window.location.hash.substring(custom_prefix.length)); // remove #step prefix
    } else {
      id = hash.substring(1); // when the hash is not the number.
    }
  }
  show(id);
};
window.onhashchange = function(event)
{
  update_from_hash();
};


function showFooter(current, sections){
  // Enable empty footer
  let area = document.getElementsByClassName('prev-next-area')[0];
//  let footer = document.getElementsByClassName('prev-next-footer')[0];
  area.innerHTML = "";
//  footer.style.display = 'block';

  // And possibly fill it
  if (current != 1){
    area.innerHTML += '<a class="left-prev" href="javascript:show(' + (current - 1) + ')" title="previous step"> \
      <i class="fa-solid fa-angle-left"></i> \
      <div class="prev-next-info"> \
        <p class="prev-next-subtitle">previous</p> \
      </div> \
    </a>';
  }
  if (sections.length != 1 && current != sections.length - 1){
   area.innerHTML += '<a class="right-next" href="javascript:show(' + (current + 1) + ')" title="next step"> \
      <div class="prev-next-info"> \
        <p class="prev-next-subtitle">next</p> \
      </div> \
      <i class="fa-solid fa-angle-right"></i> \
    </a>';
  }
}


function show(id){
  // print("asdf")
  let sections = document.getElementsByTagName('section');
  if(sections.length < 2) {
    return;
  }
  for (i = 1; i < sections.length; ++i){
    sections[i].style.display = 'none';
  }
  if(typeof id === 'string'){ // when the hash is not the number. This will convert it to the num of the section.
    for (i = 1; i < sections.length; ++i){
      if(sections[i].id === id){
        id = i;
        break;
      }
    }
  }
  sections[id].style.display = 'block';
  showFooter(id, sections);
  window.location.hash = custom_prefix + id;
}

function get_static_path() {
  var scripts= document.getElementsByTagName('script');
  var path= scripts[scripts.length-1].src.split('?')[0];      // remove any ?query
  console.log(path);

  let x=0;
  path= path.split('/').slice(0, -1).join('/')+'/';  // remove last filename part of path

  while(!path.endsWith('_static/') && x<3) {
  path= path.split('/').slice(0, -2).join('/')+'/';  // remove last folder part of path
  console.log(path);
  x++;
  }
  return path;
}


global_article_data = null;

function get_articles() {
  var path= get_static_path();
fetch(`${path}js/articles.json`)
.then(response => response.json())
.then(data => {
  global_article_data = data;

  create_lang_switcher(get_current_lang(data), data);
});
}

function get_current_lang(article_data) {
  let current_url = window.location.href;
  let current_url_parts = current_url.split('/');
  current_url_parts = current_url_parts.filter((part) => article_data.languages.map((l) => l.short).includes(part));
  return current_url_parts[0];
}

function create_lang_switcher(lang, article_data) {
  console.log(lang);
  let header = document.getElementsByClassName('article-header-buttons')[0];
  let options = article_data.languages.map((l) => {
    return `<option value="${l.short}" ${l.short == lang? "selected" : ''}>${l.long}</option>`;
  });
  let lang_selector = `<select id="lang-selector" onchange="change_lang('${lang}', this.value)"> ${options.join('')} </select>`;
  appendHtml(header, lang_selector);
}

function change_lang(old_lang, new_lang) {
  let current_url = window.location.href;
  let new_url = current_url.replace(`/${old_lang}/`, `/${new_lang}/`);
  window.location = new_url;
}

// assemble page has a lot of images that are not shown until you get to that step. Lazy loading makes the page load faster (js is loaded last)
// this function will remove the loading="lazy" attribute from all the images on the page so they will load after the page is loaded.
function load_lazy_imgs() {
  setTimeout(() => {
    // get all the images with the loading="lazy" attribute
    let images = document.querySelectorAll('img[loading="lazy"]');
    images.forEach((img) => {
      // remove the loading attribute
      img.removeAttribute('loading');
    });
  }, 2000);
}