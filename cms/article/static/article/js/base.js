(function($){
    // Listen to .load-more bnt and
    // append articles links to table from peginate/{{page}}
    var page = 2,
        url_pattern = 'peginate/{{page}}';
        $table = $('.table');
        $btn = $('.btn.load-more');

    $btn.click(function(event){
        event.preventDefault();
        $.get(url_pattern.replace('{{page}}', page), function(data){
            if(data.trim().length > 0){
                $table.find('tbody').append(data);
                if ($table.find('[data-last]').length > 0){
                    $btn.addClass('disabled');
                } else {
                    page ++;
                }
            }
        });
    });
})($);
