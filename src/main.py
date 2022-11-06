from typing import Literal


class translate_inspection_type(object):
    def __init__(self, text_inspection, parts_changed):
        self.text_inspection = text_inspection
        self.translate_data = None
        self.parts_changed = []
        self.parts_change_condition_data = {"": {"": ""}}
        self.CRM_data = None

        self.parts_change_condition_data = self.fetch_fsys_data()

    def fetch_fsys_data(self):
        return {"": {"": ""}}

    def main(self):
        by_text_inspection = self.by_text(self.text_inspection)
        by_actual_parts_changed = self.by_actual_parts_changed(
            self.parts_changed, self.parts_change_condition_data
        )
        by_text_except_inspection = self.by_text_to_exception_inspection()
        by_CRM_inspection = self.by_CRM()

        return (
            by_text_inspection,
            by_actual_parts_changed,
            by_text_except_inspection,
            by_CRM_inspection,
        )

    # translate by text
    def by_text(
        self, text_inspection: str
    ) -> Literal["CI", "TI", "MI", "OTHER", "判定不可"]:
        if not isinstance(text_inspection, str):
            print("テキストによる読み替え不可データが存在します。")
            return "判定不可"
        else:
            if text_inspection == "Case1":
                return "MI"
            elif text_inspection == "Case2":
                return "TI"
            elif text_inspection == "Case3":
                return "CI"
            else:
                return "OTHER"

    # translate by actual parts change and condition by unit
    def by_actual_parts_changed(
        self, parts_changed: list[str], condition: dict[str, dict[str, str]]
    ):
        print(parts_changed, condition)  # TODO AFTER DELETE
        pass

    # translate by text (Exception Inspection)
    def by_text_to_exception_inspection(self):
        pass

    # translate bu CRM data
    def by_CRM(self):
        pass


if __name__ == "__main__":
    tit = translate_inspection_type()
