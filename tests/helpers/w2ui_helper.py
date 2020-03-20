
class W2UiHelper:
    def __init__(self, driver):
        self.driver = driver

    def select_field_value_by_id(self, field_id, field_value):
        self.driver.execute_script(" \
            let inputDataGroup = $('#' + arguments[0]).data(); \
            for (let groupItem of inputDataGroup.w2field.options.items) { \
                if (groupItem.id == arguments[1]) { \
                    inputDataGroup.selected = groupItem; \
                } \
            } \
            inputDataGroup.w2field.refresh(); \
            ", field_id, field_value)

    def append_field_value_by_id(self, field_id, field_value):
        self.driver.execute_script(" \
            let itemData = $('#' + arguments[0]).data(); \
            \
            let groupItemExists = false; \
            for (let groupItem of itemData.w2field.options.items) { \
                if (groupItem.id == arguments[1]) { \
                    groupItemExists = true; \
                } \
            } \
            \
            if (!groupItemExists) { \
                itemData.w2field.options.items.push({id: arguments[1], text: arguments[1], hidden: false}); \
            } \
            \
            itemData.w2field.refresh(); \
        ", field_id, field_value)
