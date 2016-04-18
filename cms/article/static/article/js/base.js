(function($){
    var page = 1,
        url_pattern =  'paginate/{{page}}';
        $table = $('.table');

    $('.load-more').click(function(event){
        console.log('here!');
        $.get(url_pattern.replace('{{page}}', page), function(data){
            if(data.length > 0){
                $table.find('tbody').append(data);
                page ++;
            }
        });
    });
})($);
