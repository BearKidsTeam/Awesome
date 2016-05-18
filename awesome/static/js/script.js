jQuery(function($) {
  var $bodyEl = $('body'),
      $sidedrawerEl = $('#sidedrawer');
  
  
  // ==========================================================================
  // Toggle Sidedrawer
  // ==========================================================================
  function showSidedrawer() {
    // show overlay
    var options = {
      onclose: function() {
        $sidedrawerEl
          .removeClass('active')
          .appendTo(document.body);
      }
    };
    
    var $overlayEl = $(mui.overlay('on', options));
    
    // show element
    $sidedrawerEl.appendTo($overlayEl);
    setTimeout(function() {
      $sidedrawerEl.addClass('active');
    }, 20);
  }
  
  
  function hideSidedrawer() {
    $bodyEl.toggleClass('hide-sidedrawer');
  }
  
  
  $('.js-show-sidedrawer').on('click', showSidedrawer);
  $('.js-hide-sidedrawer').on('click', hideSidedrawer);
  
  
  // ==========================================================================
  // Animate menu
  // ==========================================================================
  var $titleEls = $('strong', $sidedrawerEl);
  
  $titleEls
    .next()
    .hide();
  
  $titleEls.on('click', function() {
    $(this).next().slideToggle(200);
  });
  
// ==========================================================================
// Header Nav Fix
// ==========================================================================

$(window.document).scroll(function () {
	var scroll_top = $(document).scrollTop(); 
	if (scroll_top <= 80) {
		$("#header").addClass("header-nocolor");
		$("#header").removeClass("header-color");
	} else {
		$("#header").removeClass("header-nocolor");
		$("#header").addClass("header-color");
	}
});

// ==========================================================================
// Scroll Fix
// ==========================================================================

$('a').click(function () {
	var target = $(this).attr('href');
	if (target[0]=="#") {
		$("html,body").animate({scrollTop:($(target).offset().top-50)}, 261);
	}
});
  
});


