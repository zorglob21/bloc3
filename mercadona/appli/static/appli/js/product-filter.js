$(document).ready(function(){
  $(".filter-checkbox, #priceFilterBtn").on('click', function(){
    var _filterObj={};
    var _minPrice=$('#minPrice').attr('min');
    var _maxPrice=$('#maxPrice').val();
    _filterObj.minPrice=_minPrice;
		_filterObj.maxPrice=_maxPrice;
    $(".filter-checkbox").each(function(index,ele){
      var _filterVal= $(this).val()
      var _filterKey= $(this).data('filter');
      _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
        return el.value;
    });

  });
  console.log(_filterObj);
  console.log()
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
    //  $(".ajaxLoader").hide();
    }
  });
});

$("#maxPrice").on('blur',function(){
  var _min=$(this).attr('min');
  var _max=$(this).attr('max');
  var _value=$(this).val();
  console.log(_value,_min,_max);
  if(_value < parseInt(_min) || _value > parseInt(_max)){
    alert('Valeurs devraient être entre :'+_min+' et '+_max);
    $(this).val(_min);
    $(this).focus();
    $("#rangeInput").val(_min);
    return false;
  }
});

});