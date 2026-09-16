(function ($) {

	$(function () {

		$('.post-carousel').each(function () {
			var $carousel = $(this);
			var $track = $carousel.find('.post-carousel-track');
			var $slides = $carousel.find('.post-carousel-slide');
			var $dots = $carousel.find('.post-carousel-dot');
			var index = 0;

			function go(i) {
				index = (i + $slides.length) % $slides.length;
				$track.css('transform', 'translateX(-' + (index * 100) + '%)');
				$dots.removeClass('active').eq(index).addClass('active');
			}

			$dots.eq(0).addClass('active');

			$carousel.find('.post-carousel-prev').on('click', function () {
				go(index - 1);
			});

			$carousel.find('.post-carousel-next').on('click', function () {
				go(index + 1);
			});

			$dots.on('click', function () {
				go($dots.index(this));
			});

			var startX = null;

			$track.on('touchstart', function (e) {
				startX = e.originalEvent.touches[0].clientX;
			});

			$track.on('touchend', function (e) {
				if (startX === null) return;
				var dx = e.originalEvent.changedTouches[0].clientX - startX;
				if (Math.abs(dx) > 40) go(index + (dx < 0 ? 1 : -1));
				startX = null;
			});

		});

	});

})(jQuery);
