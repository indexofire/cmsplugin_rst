// -------------------------------------------------------------------
// markItUp!
// -------------------------------------------------------------------
// Copyright (C) 2008 Jay Salvat
// http://markitup.jaysalvat.com/
// -------------------------------------------------------------------
// ReStructured Text
// http://docutils.sourceforge.net/
// http://docutils.sourceforge.net/rst.html
// -------------------------------------------------------------------
// Mark Renron <indexofire@gmail.com>
// http://www.indexofire.com
// -------------------------------------------------------------------
myReSTSettings = {
    nameSpace: 'ReST',
	previewParserPath: '',
	onShiftEnter: {keepDefault:false, openWith:'\n\n'},
	markupSet: [
        {name:'Level 1 Heading', key:'1', placeHolder:'Your title Here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '=') } },
        {name:'Level 2 Heading', key:'2', placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '-') } },
        {name:'Level 3 Heading', key:'3', placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '^') } },
        {name:'Level 4 Heading', key:'4', placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '#') } },
        {name:'Level 5 Heading', key:'5', placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '*') } },
        {name:'Level 6 Heading', key:'6', placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '$') } },
        {separator:'---------------' },
        {name:'Bold', key:'B', openWith:'**', closeWith:'**', placeHolder:'Input Your Bold Text Here...'},
        {name:'Italic', key:'I', openWith:'`', closeWith:'`', placeHolder:'Input Your Italic Text Here...'},
        {separator:'---------------' },
        {name:'Bulleted List', openWith:'- ' },
        {name:'Numeric List', openWith:function(markItUp) { return markItUp.line+'. '; } },
        {separator:'---------------' },
        {name:'Picture', key:'P', openWith:'.. image:: ', placeHolder:'Link Your Images Here...'},
        {name:'Link', key:"L", openWith:'`', closeWith:'`_ \n\n.. _`Link Name`: [![Url:!:http://]!]', placeHolder:'Link Name' },
        {name:'Content', openWith:'.. contents:: [![Contents Title]!]\n   [![Define title depth level:!::depth:]!]\n\n'},
        {name:'Code', openWith:'.. code:: [![Your Code Lexar:!:python]!]\n   [![If You Do not Need Line Numbers, Leave BLANK here:!::linenos:]!]\n\n   ',},
        {separator:'---------------'},
        {name:'Preview', call:'preview', className:"preview"},
	]
}

// mIu nameSpace to avoid conflict.
miu = {
	markdownTitle: function(markItUp, char) {
		heading = '';
		n = $.trim(markItUp.selection||markItUp.placeHolder).length;
		for(i = 0; i < n; i++) {
			heading += char;
		}
		return '\n'+heading;
	}
}
