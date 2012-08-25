(function(a,b){
	$(".del-disc").click(function(){
		var url = $(this).data("url");
		var self = $(this);
		$.post(url, {pk: 2}, function(data){
			if(data.success == true){
				self.parent().parent().remove();
			}else{
				alert("Error! 请使用后台删除.");
			}
		});
		return false;
	});
})(jQuery);