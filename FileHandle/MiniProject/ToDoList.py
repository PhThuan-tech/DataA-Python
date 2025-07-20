import json
import os.path

# Khi chay load file tasks de xem con task nao ko
FILE_DATA = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_DATA):
        if os.path.getsize(FILE_DATA) == 0:
            return []  # file rỗng, return list trống

        with open(FILE_DATA, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# add them phan todolist vao dung append
def add_tasks(tasks):
    new_task = input("Nhập tên việc cần làm:")
    tasks.append({
        "task" : new_task,
        "done" : False
    })
    print("Đã thêm task thành công")

# chuc nang luu lai taks vao file
def save_tasks(tasks):
    with open(FILE_DATA, "w", encoding="utf-8") as file:
        json.dump(tasks,file,ensure_ascii=False, indent=4)

# TODOLIST can co xem list (trang thai va ten viec can lam)
def show_lists(tasks):
    # neu list la rong thi return "danh sach rong"
    if not tasks:
        print("Danh sách đang trống!")
        return      # thoat vong lap neu rong
    print("\nDanh sách công việc cụ thể")
    for i, task in enumerate(tasks, 1):
        status = "V" if task["done"] else "X"
        print(f"{i}. {task['task']} - {status}")

# gio thi thao tac danh dau hoan thanh task
def mark_done(tasks):
    show_lists(tasks)
    try:
        idx = int(input("Nhập số thứ tự task đã hoàn thành: "))
        tasks[idx - 1]["done"] = True
        print("✔️ Đã cập nhật!")
    except:
        print(" Lỗi! Kiểm tra lại số thứ tự.")


def delete_task(tasks):
    show_lists(tasks)
    try:
        idx = int(input("Nhập số thứ tự task cần xóa: "))
        task = tasks.pop(idx - 1)
        print(f"🗑 Đã xóa task: {task['task']}")
    except:
        print("Lỗi! Kiểm tra lại số thứ tự.")

def main():
    tasks = load_tasks()

    while True:
        print("\n TO-DO MENU")
        print("1. Xem task")
        print("2. Thêm task")
        print("3. Đánh dấu hoàn thành")
        print("4. Xóa task")
        print("5. Thoát")

        choice = input("Chọn chức năng (1-5): ")

        if choice == '1':
            show_lists(tasks)
        elif choice == '2':
            add_tasks(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Đã lưu và thoát. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
