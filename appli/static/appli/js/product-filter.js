$(document).ready(function(){
  $(".filter-checkbox, #priceFilterBtn").on('click', function(){
    var _filterObj={};
    
    var _maxPrice=$('#maxPrice').val();

		_filterObj.maxPrice=_maxPrice;
    $(".filter-checkbox").each(function(index,ele){
      var _filterVal= $(this).val()
      var _filterKey= $(this).data('filter');
      _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
        return el.value;
    });

  });
  console.log(_filterObj);
  console.log('test')
  //Run Ajax
  $.ajax({
    url: 'filter-data',
    data: _filterObj,
    dataType: 'json',
    beforeSend:function(){
      $("#filteredProducts").html('Loading...');
     
    },
    success:function(res){
      console.log(res);
      $("#filteredProducts").html(res.data);
   
    }
  });
});

$("#maxPrice").on('blur',function(){

  var _max=$(this).attr('max');
  var _value=$(this).val();
  console.log(_value,_max);
  if(_value > parseInt(_max)){
    alert('Valeurs devraient être en dessous de :'+_max);
  
    $(this).focus();

    return false;
  }
});

});