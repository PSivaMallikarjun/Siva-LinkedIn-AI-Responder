import os


from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from siva_linkedin_ai_responder.tools.phantom_buster_send_reply_tool import PhantomBusterSendReplyTool
from siva_linkedin_ai_responder.tools.google_sheets_append_row_tool import GoogleSheetsAppendRowTool
from siva_linkedin_ai_responder.tools.unipile_send_message_tool import UnipileSendMessageTool





@CrewBase
class SivaLinkedinAiResponderCrew:
    """SivaLinkedinAiResponder crew"""

    
    @agent
    def linkedin_message_classification_specialist(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["linkedin_message_classification_specialist"],
            
            
            tools=[],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-5.6-luna",
                
                
            ),
            
        )
        
    
    @agent
    def siva_s_personal_linkedin_voice_agent(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["siva_s_personal_linkedin_voice_agent"],
            
            
            tools=[],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-5.6-luna",
                
                
            ),
            
        )
        
    
    @agent
    def linkedin_outbound_message_dispatcher(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["linkedin_outbound_message_dispatcher"],
            
            
            tools=[				PhantomBusterSendReplyTool(),
				UnipileSendMessageTool()],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-5.6-luna",
                
                
            ),
            
        )
        
    
    @agent
    def conversation_log_manager(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["conversation_log_manager"],
            
            
            tools=[				GoogleSheetsAppendRowTool()],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-5.6-luna",
                
                
            ),
            
        )
        
    

    
    @task
    def classify_linkedin_message(self) -> Task:
        return Task(
            config=self.tasks_config["classify_linkedin_message"],
            markdown=False,
            
            
        )
    
    @task
    def draft_linkedin_reply(self) -> Task:
        return Task(
            config=self.tasks_config["draft_linkedin_reply"],
            markdown=False,
            
            
        )
    
    @task
    def send_reply_via_unipile(self) -> Task:
        return Task(
            config=self.tasks_config["send_reply_via_unipile"],
            markdown=False,
            
            
        )
    
    @task
    def log_interaction_to_google_sheets(self) -> Task:
        return Task(
            config=self.tasks_config["log_interaction_to_google_sheets"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the SivaLinkedinAiResponder crew"""

        # Custom manager agent for hierarchical process
        manager_agent = Agent(
            role="Crew Manager",
            goal="Coordinate the team to achieve the objective efficiently",
            backstory="An experienced manager skilled in delegation and coordination",
            llm=LLM(model="openai/gpt-5.6-luna"),
            allow_delegation=True,
        )

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.hierarchical,
            verbose=True,


            manager_agent=manager_agent,


            chat_llm=LLM(model="openai/gpt-5.6-luna"),
        )


