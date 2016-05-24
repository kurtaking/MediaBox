/* This file is to initiate all necessary javascript components for the website */

(function($){
    $(function(){
        // Initialize collapse button
        $(".button-collapse").sideNav();

        // Initialize collapsible (uncomment the line below if you use the dropdown variation)
        $('.collapsible').collapsible();

        // Initialize the modal that adds a new vinyl
        $('.modal-trigger').leanModal();

        $('.tooltipped').tooltip({delay: 50});

    }); // end of document ready
})(jQuery); // end of jQuery name space

