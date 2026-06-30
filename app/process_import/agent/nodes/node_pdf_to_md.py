import sys
from app.core.logger import logger
from app.process_import.agent.state import ImportGraphState
from app.utils.format_utils import format_state
from app.utils.task_utils import add_running_task, add_done_task



def node_pdf_to_md(state: ImportGraphState) -> ImportGraphState:
    """ 节点: PDF转Markdown (node_pdf_to_md)
    为什么叫这个名字: 核心任务是将 PDF 非结构化数据转换为 Markdown 结构化数据。
    未来要实现:
    1. 调用 MinerU (magic-pdf) 工具。
    2. 将 PDF 转换成 Markdown 格式。
    3. 将结果保存到 state["md_content"]。
    """
    # 动态获取函数名避免硬编码
    func_name = sys._getframe().f_code.co_name
    # 节点启动日志，打印当前工作流状态
    logger.debug(f"【{func_name}】节点启动，\n当前工作流状态：{format_state(state)}")
    # 开始：记录节点运行状态
    add_running_task(state["task_id"], func_name)

    try:


        pass

    except Exception as e:
        # 异常日志分级，精准提示配置问题
        logger.error(f"【{func_name}】PDF转MD流程执行失败：{str(e)}", exc_info=True)
        raise  # 抛出异常，终止工作流
    finally:
        # 结束：记录节点运行状态
        add_done_task(state["task_id"], func_name)
        # 节点完成日志，打印当前工作流状态
        logger.debug(f"【{func_name}】节点执行完成，\n更新后工作流状态：{format_state(state)}")
    
    return state
