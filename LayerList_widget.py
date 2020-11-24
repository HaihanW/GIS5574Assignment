
function buildLayerList() {
          var items = arrayUtils.map(layer.layerInfos, function(info, index) {
            if (info.defaultVisibility) {
              visible.push(info.id);
            }
            return "<input type='checkbox' class='list_item'" + (info.defaultVisibility ? "checked=checked" : "") + "' id='" + info.id + "'' /><label for='" + info.id + "'>" + info.name + "</label>";
          });
          var ll = dom.byId("layer_list");
          ll.innerHTML = items.join(' ');
          layer.setVisibleLayers(visible);
          on(ll, "click", updateLayerVisibility);
        }

        function updateLayerVisibility() {
          var inputs = query(".list_item");
          var input;
          visible = [];

          arrayUtils.forEach(inputs, function(input) {
            if (input.checked) {
              visible.push(input.id);
            }
          });
          if (visible.length === 0) {
            visible.push(-1);
          }
          layer.setVisibleLayers(visible);
        }
